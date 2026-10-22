# My Skills

BoosaIDonng 的个人 AI 技能库。换电脑或工作环境后，让 AI 阅读本仓库，即可安装全部或指定的技能。

收录策略：从各技能的上游 GitHub 仓库获取当前默认分支最新提交，保留完整技能目录及许可证。
本次获取日期：**2026-10-22**。精确提交号见 [sources.json](sources.json)。
这是获取时的最新版本快照；上游今后的新提交需要显式同步到本仓库。

## 技能与上游

| 技能 | 用途 | 上游 GitHub 位置 |
| --- | --- | --- |
| academic-research-suite | 学术研究、论文写作、审稿、系统综述筛选与实验规划 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex/tree/main/skills/academic-research-suite) |
| diagnosing-bugs | 难复现故障与性能回退的诊断流程 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) |
| karpathy-guidelines | 思考后编码、保持简单、控制改动范围与验证目标 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines) |
| ponytail | 优先复用、标准库和原生功能，减少不必要的代码 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/main/skills/ponytail) |

学术套件使用作者维护的 **Codex 原生版本**；原始 Claude Code 项目是
[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)。
Karpathy Guidelines 的旧地址 `forrestchang/andrej-karpathy-skills` 现重定向至 `multica-ai`。
技能正文保持上游原样；学术技能额外携带上游根目录的 `VERSION`、许可证与声明。

## 下次直接发给 AI

复制下面这段话，把“全部”替换成所需技能名称即可：

```text
请读取我的技能仓库 https://github.com/BoosaIDonng/my-skills，
先阅读 README.md 和 AGENTS.md，再为当前 Codex 环境安装全部技能。
使用仓库中 install.py 的安装流程，保留每个技能的完整目录和许可证。
如果只需要部分技能，就只安装我点名的技能。
如果目标位置已有同名技能，先比较版本并保留备份，不要直接覆盖。
安装后检查 SKILL.md 和配套文件，告诉我安装结果。
```

本仓库为私有仓库。新环境需先通过 GitHub CLI、SSH 或已连接的 GitHub 工具取得访问权限。
不要把访问令牌写进 URL、命令记录或仓库。

## 手动安装

需要 Git 和 **Python 3.9 或更新版本**。安装器仅使用标准库。
以下命令适用于 macOS/Linux；Windows 可将 `python3` 换成已安装的 `python` 或 `py -3`。

```bash
git clone https://github.com/BoosaIDonng/my-skills.git
cd my-skills
python3 install.py --list
python3 install.py
```

只安装指定技能：

```bash
python3 install.py karpathy-guidelines ponytail
```

查看计划，或安装到指定位置：

```bash
python3 install.py --dry-run
python3 install.py --dest /path/to/skills diagnosing-bugs
```

默认安装到 `$CODEX_HOME/skills`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。
安装器会在复制前检查所有选定技能，遇到已有同名目录就停止，避免覆盖当前安装。
安装后开启新的 Codex 对话，再显式使用 `$academic-research-suite` 等技能名称。
安装过程只复制技能文件；学术套件内额外工具的依赖按具体工作流需要安装。

如果当前 Codex 已带有内置技能安装器，也可按指定路径安装：

```bash
python3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo BoosaIDonng/my-skills --ref main --method git \
  --path skills/academic-research-suite skills/diagnosing-bugs \
         skills/karpathy-guidelines skills/ponytail
```

## 同步更新

可以对 AI 说：

```text
请按 sources.json 中的上游地址，把 my-skills 收录的四个技能同步到各自默认分支的最新提交。
复制对应的完整技能目录，保留上游许可证和署名，更新 sources.json 和 checksums.sha256，
运行 python3 test_install.py。不要把旧环境的本地修改混入上游快照。
```

`sources.json` 记录精确提交及技能文件的 Git blob；`checksums.sha256` 记录本仓库收录的每个技能文件。
验证迁移安装流程：`python3 test_install.py`。

## 许可证

原作者和上游许可证保持有效，详见 [THIRD_PARTY.md](THIRD_PARTY.md)。
学术套件采用 **CC BY-NC 4.0（署名—非商业性使用）**；其他三个技能在上游声明为 MIT。
本仓库的原创安装脚本和说明采用根目录的 MIT 许可证；该许可不改变第三方技能的许可条件。
