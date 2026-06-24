from datetime import datetime

def get_weather_description(code):
    if code == 0:
        return "clear skies"
    elif code in [1, 2, 3]:
        return "partly cloudy"
    elif code in [45, 48]:
        return "foggy"
    elif code in [51, 53, 55]:
        return "light drizzle"
    elif code in [61, 63, 65]:
        return "rainy"
    elif code in [80, 81, 82]:
        return "heavy showers"
    elif code in [95, 96, 99]:
        return "thunderstorms"
    else:
        return "mixed conditions"
    
def get_weather_opener(code):
    if code == 0 or code in [1, 2, 3]:
        return "A good day to be alive."
    elif code in [61, 63, 65, 80, 81, 82]:
        return "Grab your umbrella before you leave."
    elif code in [95, 96, 99]:
        return "Might want to stay indoors today."
    elif code in [45, 48]:
        return "A foggy one out there — drive carefully."
    else:
        return "Stay safe out there."
    
def build_email(name, rates,crude, weather):
    date_str= datetime.now().strftime("%A,%B,%d,%Y")
    time_str= datetime.now().strftime("%I:%M %p")

    description = get_weather_description(weather["code"])
    opener = get_weather_opener(weather["code"])

    change_arrow = "▲" if crude["change"] >= 0 else "▼"
    change_color =  "#1D9E75" if crude["change"] >= 0 else "#D85A30"

    html =f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 560px; margin: 0 auto; padding: 0;">
        
        <table width="100%" cellpadding="0" cellspacing="0" style="background: #0a0a0a;">
            <tr>
                <td style="padding: 1.5rem 2rem; vertical-align: top;">
                    <p style="color: #f5f0e8; font-size: 20px; font-weight: 500; margin: 0;">Early Hours</p>
                    <p style="color: #888; font-size: 12px; margin: 4px 0 0;">Your Lagos morning brief</p>
                </td>
                <td style="padding: 1.5rem 2rem 1.5rem 0; vertical-align: top; text-align: right; white-space: nowrap;">
                    <p style="color: #888; font-size: 11px; margin: 0;">{date_str}</p>
                </td>
            </tr>
        </table>

        <div style="padding: 1.75rem 2rem 1.25rem;">
            <p style="font-size: 15px; font-weight: 500; margin: 0 0 4px;">Good morning, {name}.</p>
            <p style="font-size: 14px; color: #555; margin: 0; line-height: 1.6;">
                The weather in Lagos today is <strong>{description} with a high of {weather["temp"]}°C</strong>. {opener}
            </p>
        </div>

        <hr style="border: none; border-top: 0.5px solid #e0e0e0; margin: 0 2rem;">

        <div style="padding: 1.25rem 2rem;">
            <p style="font-size: 11px; font-weight: 500; color: #888; letter-spacing: 0.8px; text-transform: uppercase; margin: 0 0 1rem;">Exchange Rates &nbsp;·&nbsp; As at {time_str}</p>
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="width: 50%; padding: 6px 8px 6px 0;">
                        <div style="background: #f5f5f5; border-radius: 8px; padding: 12px 14px;">
                            <p style="font-size: 12px; color: #888; margin: 0 0 4px;">USD / NGN</p>
                            <p style="font-size: 18px; font-weight: 500; margin: 0;">₦{rates["USD"]:,.2f}</p>
                        </div>
                    </td>
                    <td style="width: 50%; padding: 6px 0 6px 8px;">
                        <div style="background: #f5f5f5; border-radius: 8px; padding: 12px 14px;">
                            <p style="font-size: 12px; color: #888; margin: 0 0 4px;">EUR / NGN</p>
                            <p style="font-size: 18px; font-weight: 500; margin: 0;">₦{rates["EUR"]:,.2f}</p>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td style="width: 50%; padding: 6px 8px 6px 0;">
                        <div style="background: #f5f5f5; border-radius: 8px; padding: 12px 14px;">
                            <p style="font-size: 12px; color: #888; margin: 0 0 4px;">GBP / NGN</p>
                            <p style="font-size: 18px; font-weight: 500; margin: 0;">₦{rates["GBP"]:,.2f}</p>
                        </div>
                    </td>
                    <td style="width: 50%; padding: 6px 0 6px 8px;">
                        <div style="background: #f5f5f5; border-radius: 8px; padding: 12px 14px;">
                            <p style="font-size: 12px; color: #888; margin: 0 0 4px;">CNY / NGN</p>
                            <p style="font-size: 18px; font-weight: 500; margin: 0;">₦{rates["CNY"]:,.2f}</p>
                        </div>
                    </td>
                </tr>
            </table>
        </div>

        <hr style="border: none; border-top: 0.5px solid #e0e0e0; margin: 0 2rem;">

        <div style="padding: 1.25rem 2rem;">
            <p style="font-size: 11px; font-weight: 500; color: #888; letter-spacing: 0.8px; text-transform: uppercase; margin: 0 0 1rem;">Energy</p>
            <div style="background: #f5f5f5; border-radius: 8px; padding: 12px 14px; display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <p style="font-size: 12px; color: #888; margin: 0 0 4px;">Brent Crude</p>
                    <p style="font-size: 18px; font-weight: 500; margin: 0;">${crude["price"]} <span style="font-size: 13px; color: #888;">/ barrel</span></p>
                </div>
                <div style="text-align: right;">
                    <p style="font-size: 12px; color: #888; margin: 0 0 4px;">24h change</p>
                    <p style="font-size: 15px; font-weight: 500; margin: 0; color: {change_color};">{change_arrow} {abs(crude["change"])}%</p>
                </div>
            </div>
        </div>

        <hr style="border: none; border-top: 0.5px solid #e0e0e0; margin: 0 2rem;">

        <div style="padding: 1.25rem 2rem 1.75rem;">
            <p style="font-size: 13px; color: #888; margin: 0; text-align: center;">
                Have a productive day. <span style="color: #0a0a0a;">❤️ Early Hours</span>
            </p>
        </div>

    </body>
    </html>
    """
    return html

