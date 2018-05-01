# jenkins2 memo

## インストール

DIND(docker in docker)とDOOD(docker outside of docker)でjenkinsのdockerコンテナを作成しないと、
jenkinsからdockerを使用できない。

今回は、DOODを使用。
DOODの場合は、docker host側の/var/run/docker.sockをマウントしてあげなくてはいけない。

```bash
DOCKER_GID=`docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock toto1310/simple-jenkins-dood bash -c "stat -c %g /var/run/docker.sock"`
docker run -d --name jenkins \
 --group-add ${DOCKER_GID} \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -v ${PWD}/jenkins_home:/var/jenkins_home \
 -p 8080:8080 \
 -p 50000:50000 \
 toto1310/simple-jenkins-dood
```


＜参考＞
https://qiita.com/sugiyasu-qr/items/85a1bedb6458d4573407

## Jobの作成

* フリースタイル  これだと、Pipelineが設定できなかった
* GitHub Organization  これだと、githubのwebhookとかを設定できなかった（ビルド・トリガーの設定ができない）
* Pipeline  これでやるべきなのかな

## pip

jenkinsから起動したdockerで、`pip install -r requiremrents.txt`を実行すると、以下のエラー
`Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/site-packages/apipkg.py'`
うーん、どうしようかな。sudoもできないしな…自分で、docker imageを作成するしかないかぁ