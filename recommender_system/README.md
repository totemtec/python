# recommender-system

源码来自：

https://github.com/milvus-io/bootcamp/tree/master/applications/nlp/recommender_system

### ipynb 运行问题

`rye sync` 后，运行 `jupyter notebook` 中的脚本出错，提示找不到 `ipykernel`

```bash
rye install jupyter --include-dep jupyter-core
```

上述命令运行后，虚拟环境目录下，并未发现 `ipykernel`，尝试使用下面方法可以运行

给本项目安装 jupyter 运行环境

```bash
rye add --sync ipykernel
rye add --sync ipywidgets
```
