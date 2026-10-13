# LangGraph 课程环境

## 当前配置

- 项目目录：`D:\LangGraph\langgraph`
- Conda 根目录：`D:\LangGraph\.tools\miniconda3`（Conda 26.5.3）
- Conda 环境：`langgraph`（Python 3.13.16）
- PyCharm：2026.2.3
- PyCharm 项目解释器：`D:\LangGraph\.tools\miniconda3\envs\langgraph\python.exe`
- Jupyter 内核：`Python (langgraph)`
- 依赖来源：课程提供的 `requirements_full.txt`
- pip 镜像：清华源，仅作用于此 Conda 环境

## 重新创建环境

在重新打开的 PowerShell 中运行：

```powershell
conda env create -f environment.yml
conda activate langgraph
python -m pip config --site set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install -r requirements_full.txt
python -m ipykernel install --user --name langgraph --display-name "Python (langgraph)"
```

本机已通过 `conda init powershell` 配置 PowerShell。首次初始化后需重新打开 PowerShell，才能使用 `conda activate`。

## API Key

把自己的 DeepSeek API Key 填入项目根目录 `.env` 中的 `DEEPSEEK_API_KEY=`。当前文件留空；没有进行真实模型调用。

## 版本说明

截至 2026-10-13，官方目录中 Python 3.13 对应的 Miniconda 安装包为 26.7.1-1，本机安装的 Conda 为 26.5.3。PyCharm 2026.2.3 已是官方当前稳定版；资料目录附带的 PyCharm 2026.1.3 安装包较旧。

课程依赖文件中的 LangChain 1.2.12 和 LangGraph 1.1.2 低于 PyPI 当前版本（分别为 1.4.1 和 1.2.14）。为保持课程兼容性，这里保留课程固定版本，没有自动升级整个依赖清单。升级前应先验证课程代码兼容性。
