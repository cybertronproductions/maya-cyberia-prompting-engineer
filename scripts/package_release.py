"""Build and verify the public downloads without changing skill or prompt text."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "_tmp" / "dist"
SKILL = "skills/maya-cyberia-prompting-engineer/"


def tracked(*paths):
    names = subprocess.check_output(
        ["git", "ls-files", "-z", "--", *paths], cwd=ROOT
    ).decode().split("\0")
    return {name: ROOT / name for name in names if name}


def package(destination, files):
    assert files, "Empty package"
    with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
        for name, source in sorted(files.items()):
            path = PurePosixPath(name)
            assert not path.is_absolute() and ".." not in path.parts
            assert not source.is_symlink() and source.is_file(), source
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    with ZipFile(destination) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(files)
        for name, source in files.items():
            assert archive.read(name) == source.read_bytes(), name


def main():
    DIST.mkdir(parents=True, exist_ok=True)
    version = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]
    assert version == json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
    skill = tracked(SKILL)
    assert SKILL + "SKILL.md" in skill
    assert SKILL + "references/prompts-exemplos.md" in skill
    plugin = tracked("plugin.json", "README.md", "LICENSE", ".claude-plugin", "assets")
    plugin.update(skill)
    assert ".claude-plugin/plugin.json" in plugin
    package(DIST / "maya-cyberia-plugin.zip", plugin)
    # Keep already-shared /latest/download URLs working across releases.
    (DIST / "maya-cyberia-1.0.0.zip").write_bytes((DIST / "maya-cyberia-plugin.zip").read_bytes())
    skill_only = {name.removeprefix("skills/"): source for name, source in skill.items()}
    skill_only["maya-cyberia-prompting-engineer/LICENSE"] = ROOT / "LICENSE"
    package(DIST / "maya-cyberia-skill.zip", skill_only)
    chatgpt = {name.removeprefix("chatgpt/"): source for name, source in tracked("chatgpt/instructions.md", "chatgpt/knowledge").items()}
    chatgpt["LEIA-ME.txt"] = ROOT / "chatgpt/LEIA-ME.txt"
    chatgpt["LICENSE"] = ROOT / "LICENSE"
    assert len(chatgpt) == 7
    package(DIST / "maya-cyberia-chatgpt-projeto.zip", chatgpt)
    for name in ("maya-cyberia-skill.zip", "maya-cyberia-chatgpt-projeto.zip"):
        (ROOT / "docs" / name).write_bytes((DIST / name).read_bytes())
    names = ("maya-cyberia-plugin.zip", "maya-cyberia-1.0.0.zip", "maya-cyberia-skill.zip", "maya-cyberia-chatgpt-projeto.zip")
    checksums = "".join(f"{hashlib.sha256((DIST / name).read_bytes()).hexdigest()}  {name}\n" for name in names)
    (DIST / "SHA256SUMS.txt").write_text(checksums, encoding="utf-8")
    print(f"v{version}: 4 packages verified; downloads updated in docs/")
    print(checksums, end="")


if __name__ == "__main__":
    main()
