def makeHtml(account_type, leftElectricity, leftMoney, warning_threshold):
    html =  f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>电费余额提醒通知</title>
        <style>
            body {{ font-family: "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            .header {{ background-color: #f5f7fa; padding: 15px 20px; border-radius: 6px 6px 0 0; border-left: 4px solid #4285f4; }}
            .header h1 {{ margin: 0; color: #2c3e50; font-size: 20px; }}
            .content {{ padding: 20px; border: 1px solid #eee; border-top: none; border-radius: 0 0 6px 6px; }}
            .warning {{ color: #e74c3c; font-weight: bold; padding: 10px; background-color: #fef5f5; border-left: 3px solid #e74c3c; margin: 15px 0; }}
            .info-item {{ margin: 12px 0; }}
            .label {{ display: inline-block; width: 100px; color: #666; }}
            .value {{ color: #2c3e50; }}
            .footer {{ margin-top: 20px; padding-top: 15px; border-top: 1px dashed #eee; color: #999; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>电费余额提醒通知</h1>
        </div>
        <div class="content">
            <p>尊敬的用户：</p>
            <p>您好！您的用电账户当前余额较低，请注意及时充值，避免因断电影响使用。</p>
            
            <div class="warning">
                【重要提醒】当前余额已低于预警值，请尽快处理！
            </div>
            
            <div class="info-item">
                <span class="label">宿舍号：</span>
                <span class="value">18-217</span>  <!-- 动态替换 -->
            </div>
            <div class="info-item">
                <span class="label">账户类型：</span>
                <span class="value">{account_type}</span>  <!-- 动态替换 -->
            </div>
            <div class="info-item">
                <span class="label">剩余电量：</span>
                <span class="value">{leftElectricity} 度</span>  <!-- 动态替换 -->
            </div>
            <div class="info-item">
                <span class="label">账户余额：</span>
                <span class="value">{leftMoney} 元</span>  <!-- 动态替换 -->
            </div>
            <div class="info-item">
                <span class="label">预警阈值：</span>
                <span class="value">{warning_threshold} 元</span>  <!-- 动态替换 -->
            </div>
            
            <p>充值方式：可通过校园一卡通线上缴费平台进行充值。</p>
            
            <div class="footer">
                <p>此邮件为系统自动发送，请勿直接回复。如有疑问，请联系dre4m1nd@163.com</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html