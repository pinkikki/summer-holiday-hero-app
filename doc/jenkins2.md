# jenkins2 memo

## Jobの作成

* フリースタイル  これだと、Pipelineが設定できなかった
* GitHub Organization  これだと、githubのwebhookとかを設定できなかった（ビルド・トリガーの設定ができない）
* Pipeline  これでやるべきなのかな

## Pipeline

### agent

どのノードで実施するか。
どのノードでも良い場合は、`agent any`と指定する