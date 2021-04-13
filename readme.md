# Telegram send message without joining the group

Telegram 不用加群即可发消息

POC: 仅用于展示实现方法

## Limitation

- 私密频道需要加频道以后才可以发消息
- 公开频道可以直接发送
- 管理依然可以删除你的消息
- **但是你可以绕开加群验证**

## Run Demo

```bash
pip3 install -r requirements.txt
python3 main.py
```

按照指示操作即可，首次使用需要登录，过程中只需要想要发送的讨论组频道消息即可