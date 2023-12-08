# py-architecture-as-code
<!-- Insert shield io with content Version 1.0 -->
![](https://img.shields.io/badge/version-0.1-blue)

<!-- Insert shield io with content License MIT -->
![](https://img.shields.io/badge/License-MIT-green)

<!-- Insert shield io with content Python 3.8 -->
![](https://img.shields.io/badge/Python-3.11-yellow)

# Description

Archiecture as code is a project that aims to create a tool that can generate a diagram of a deployment from YAML code using Python and Graphviz.



# Required information

## Diagram information
[Diagram Info](https://diagrams.mingrammer.com/docs/nodes/azure)

# Usage 

```sh
docker run -it --rm -v "$PWD:/app" architecture_as_code \
    python main.py --provider aws --region us-east-1 --resources ec2,rds --template custom.dot
```