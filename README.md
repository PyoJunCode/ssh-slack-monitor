# SSH-monitoring-with-slack
Simple ssh proxy connection monitoring app with slack


## Build

You have to add `.env` file in directory with `slack_token` value before build docker.

(slack bot token starts with 'xoxb', ref: [Creating Slack App](https://api.slack.com/authentication/basics))



```yaml
# example of .env file
slack_token=xoxb-XXXXXXXX-XXXXXXX-XXXXXX
```



Build docker

```bash
docker build -t <image-name> .
```







## Run



Run docker

```bash
docker run -v /var/log/auth.log:/var/log/auth.log -d <image-name>
```



If you want to change log file path (in docker), 

1. change `-v /var/log/auth.log:<PATH-YOU-WANT>`

2. give `-e LOG_PATH=<PATH-YOU-WANT> `  argument when you run docker image.

Default value of `LOG_PATH` is `/var/log/auth.log` 


## Try

![example](https://user-images.githubusercontent.com/47979730/188625537-23160aa8-5978-4b6b-9394-26e1810b2433.png)

