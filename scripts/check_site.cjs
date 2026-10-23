// Run with node scripts/check_site.cjs; no browser or dependencies required.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const html = fs.readFileSync(path.join(__dirname, '../docs/index.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
assert(!html.includes('chatgpt.com/?q='));
assert(html.includes('.claude-box:target{display:block}'));
for (const name of ['maya-cyberia-skill.zip', 'maya-cyberia-chatgpt-projeto.zip']) {
  assert(html.includes(`href="${name}" download`));
  assert(fs.existsSync(path.join(__dirname, '../docs', name)));
}

async function checkClipboard(blocked) {
  const listeners = {};
  const fields = [];
  const timers = [];
  const source = { innerText: '/plugin install maya-cyberia@maya-cyberia' };
  let copied;
  const button = {
    dataset: { copy: 'cc' }, textContent: 'Copiar comandos',
    parentElement: { querySelector: () => fields[0] },
    addEventListener: (event, handler) => { listeners.copy = handler; },
    insertAdjacentElement: (where, field) => fields.push(field),
  };
  const panels = new Map();
  const links = ['chatgpt-box', 'claude-box'].map(id => {
    panels.set('#' + id, { classList: { add: value => { assert.equal(value, 'open'); } }, focus: () => {} });
    return { getAttribute: () => '#' + id, addEventListener: (event, handler) => { listeners[id] = handler; } };
  });
  vm.runInNewContext(script, {
    document: {
      querySelectorAll: selector => selector === '[data-copy]' ? [button] : links,
      querySelector: selector => panels.get(selector),
      getElementById: () => source,
      createElement: tag => {
        assert.equal(tag, 'textarea');
        return { setAttribute: () => {}, focus: () => {}, select: () => {} };
      },
    },
    navigator: { clipboard: { writeText: async value => {
      if (blocked) throw new Error('Permission denied');
      copied = value;
    } } },
    setTimeout: callback => timers.push(callback),
  });
  listeners['chatgpt-box']();
  listeners['claude-box']();
  await listeners.copy();
  if (blocked) {
    assert.equal(fields.length, 1);
    assert.equal(fields[0].value, source.innerText);
    assert.equal(fields[0].readOnly, true);
    assert.equal(button.textContent, 'Selecione e copie o texto abaixo');
    await listeners.copy();
    assert.equal(fields.length, 1);
  } else {
    assert.equal(copied, source.innerText);
    assert.equal(button.textContent, 'Copiado');
    timers[0]();
    assert.equal(button.textContent, 'Copiar comandos');
  }
}

(async () => {
  await checkClipboard(false);
  await checkClipboard(true);
  console.log('Site checks passed: panels, download files, clipboard success and denied permission.');
})().catch(error => { console.error(error); process.exitCode = 1; });
