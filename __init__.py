from ElectricityBillPushedByEmail.Utils import makeHtml, getElectricity, emailSender
import yaml

with open("config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

lightingLimit = float(config['getElectricity']['reminderLimitedByMoney']['lighting'])
airConditioningLimit = float(config['getElectricity']['reminderLimitedByMoney']['airConditioning'])


def main():
    # 获取度数和电费数据
    lighting = list(getElectricity.getLightingElectricity())
    airConditioning = list(getElectricity.getAirConditioningElectricity())

    if float(lighting[1]) <= lightingLimit:
        html = makeHtml.makeHtml("照明", lighting[0], lighting[1], lightingLimit)
        message = emailSender.makeMessage("照明费不足通知", html)
        emailSender.sendEmail(message)

    if float(airConditioning[1]) <= airConditioningLimit:
        html = makeHtml.makeHtml("空调", airConditioning[0], airConditioning[1], airConditioningLimit)
        message = emailSender.makeMessage("空调费不足通知", html)
        emailSender.sendEmail(message)

if __name__ == '__main__':
    main()



