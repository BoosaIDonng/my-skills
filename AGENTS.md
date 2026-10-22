# Instructions for AI agents

This is BoosaIDonng's personal collection of upstream Codex skills.

## Installing

1. Read README.md and sources.json. Ask which skills only if the user has not specified a selection and the task does not imply installing all.
2. Obtain this private repository using the current environment's authorized GitHub access. Never embed credentials in URLs or committed files.
3. Run `python3 install.py --list`, then `python3 install.py --dry-run <names>` and `python3 install.py <names>`. Omit names when the user requests all skills.
4. Respect CODEX_HOME, or use `--dest` for a user-specified skills directory. Preserve complete skill directories and license files.
5. Existing destinations are protected. If an update is requested, compare versions and back up the existing skill before replacing it. Never silently delete local modifications.
6. Verify the installed SKILL.md and supporting files. Explain that a new Codex conversation loads the new installation.

The built-in Codex skill-installer may also install from `BoosaIDonng/my-skills` using explicit `skills/<name>` paths and `--method git`.

## Maintaining

- Follow the upstream repositories and paths in sources.json. Resolve the latest default-branch commit when the user requests an update; record the exact commit used.
- Use `Imbad0202/academic-research-skills-codex` for the Codex academic suite. Its sibling Claude Code distribution has a different install layout.
- Copy upstream skill files unchanged. Keep full supporting directories, notices and license conditions. Carry the academic repository's root VERSION and license/notice files with its skill.
- Do not mix machine-local skill edits into an upstream snapshot. Document intentional local adaptations separately if the user requests them.
- Update sources.json and checksums.sha256, then run `python3 test_install.py` before committing.
- Do not read all vendored workflows or execute their research/diagnosis instructions just to install them. Do not run provider/model/network experiments as part of packaging tests.
- Nested .github workflows inside a skill are upstream reference files, not this collection's CI.
