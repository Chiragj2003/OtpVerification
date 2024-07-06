import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import credential
from random import randint

def otp_generator():
    otp = randint(100000, 999999)
    return str(otp)

def otp_checker(otp):
    user_input = input("Enter the OTP: ")
    if user_input == otp:
        print("Access granted!")
    else:
        print("Access denied.")

def send_email(receiver_email, html_content):
    try:
        sender_email = credential.email_sender
        password = credential.password

        msg = MIMEMultipart("alternative")
        msg["Subject"] = "OTP for Verification"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        part = MIMEText(html_content, "html")
        msg.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def main():
    receiver_email = input("Enter the receiver's email: ")
    
    # Generate OTP
    otp = otp_generator()
    print(f"Generated OTP: {otp}")

    # Prepare HTML content
    html_content = """
    <!DOCTYPE HTML
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <!--[if gte mso 9]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!-->
  <meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
  <title></title>

  <style type="text/css">
    @media only screen and (min-width: 620px) {
      .u-row {
        width: 600px !important;
      }

      .u-row .u-col {
        vertical-align: top;
      }

      .u-row .u-col-100 {
        width: 600px !important;
      }

    }

    @media (max-width: 620px) {
      .u-row-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
      }

      .u-row .u-col {
        min-width: 320px !important;
        max-width: 100% !important;
        display: block !important;
      }

      .u-row {
        width: 100% !important;
      }

      .u-col {
        width: 100% !important;
      }

      .u-col>div {
        margin: 0 auto;
      }
    }

    body {
      margin: 0;
      padding: 0;
    }

    table,
    tr,
    td {
      vertical-align: top;
      border-collapse: collapse;
    }

    p {
      margin: 0;
    }

    .ie-container table,
    .mso-container table {
      table-layout: fixed;
    }

    * {
      line-height: inherit;
    }

    a[x-apple-data-detectors='true'] {
      color: inherit !important;
      text-decoration: none !important;
    }

    table,
    td {
      color: #000000;
    }

    #u_body a {
      color: #0000ee;
      text-decoration: underline;
    }

    @media (max-width: 480px) {
      #u_content_image_2 .v-container-padding-padding {
        padding: 40px 10px 10px !important;
      }

      #u_content_heading_1 .v-container-padding-padding {
        padding: 40px 10px 20px !important;
      }

      #u_content_heading_1 .v-font-size {
        font-size: 20px !important;
      }

      #u_content_text_2 .v-container-padding-padding {
        padding: 10px !important;
      }

      #u_content_button_1 .v-size-width {
        width: 65% !important;
      }

      #u_content_text_3 .v-container-padding-padding {
        padding: 10px !important;
      }

      #u_content_heading_2 .v-container-padding-padding {
        padding: 30px 20px 10px !important;
      }

      #u_content_heading_2 .v-text-align {
        text-align: center !important;
      }

      #u_content_social_1 .v-container-padding-padding {
        padding: 10px 0px 10px 80px !important;
      }
    }
  </style>



  <!--[if !mso]><!-->
  <link href="https://fonts.googleapis.com/css?family=Raleway:400,700&display=swap" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css2?family=Arvo&display=swap" rel="stylesheet" type="text/css">
  <!--<![endif]-->

</head>

<body class="clean-body u_body"
  style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ecf0f1;color: #000000">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table id="u_body"
    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ecf0f1;width:100%"
    cellpadding="0" cellspacing="0">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #ecf0f1;"><![endif]-->



          <div class="u-row-container" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #140173;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                  <div
                    style="background-color: #140173;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div
                      style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--<![endif]-->

                      <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <div class="v-text-align v-font-size"
                                style="font-family: andale mono,times; font-size: 24px; font-weight: 700; line-height: 140%; text-align: center; word-wrap: break-word;">
                                <p style="line-height: 140%;"><span
                                    style="text-decoration: underline; line-height: 19.6px;"><strong><span
                                        style="color: #f1c40f; line-height: 19.6px; text-decoration: underline;">OTP
                                        Verification</span></strong></span></p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div><!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>





          <div class="u-row-container" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #140173;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                  <div
                    style="background-color: #140173;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div
                      style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--<![endif]-->

                      <table id="u_content_image_2" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:80px 10px 10px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                  <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">

                                    <img align="center" border="0" src="images/image-1.png" alt="image" title="image"
                                      style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 90%;max-width: 522px;"
                                      width="522" />

                                  </td>
                                </tr>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_heading_1" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:45px 10px 20px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <!--[if mso]><table width="100%"><tr><td><![endif]-->
                              <h1 class="v-text-align v-font-size"
                                style="margin: 0px; color: #f99d05; line-height: 140%; text-align: center; word-wrap: break-word; font-family: Arvo; font-size: 23px; font-weight: 400;">
                                <span><span><span><span>WELCOME</span></span></span></span></h1>
                              <!--[if mso]></td></tr></table><![endif]-->

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_text_2" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px 50px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <div class="v-text-align v-font-size"
                                style="font-size: 14px; color: #95a5a6; line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="line-height: 140%;">Dear User,</p>
                                <p style="line-height: 140%;"> </p>
                                <p style="line-height: 140%;">Thank you for trying my project . if you like this project
                                  go to my linked in profile and GitHub profile and follow for more</p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_button_1" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <!--[if mso]><style>.v-button {background: transparent !important;}</style><![endif]-->
                              <div class="v-text-align" align="center">
                                <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://unlayer.com" style="height:37px; v-text-anchor:middle; width:180px;" arcsize="11%"  stroke="f" fillcolor="#f99d05"><w:anchorlock/><center style="color:#140173;"><![endif]-->
                                <a href="https://unlayer.com" target="_blank" class="v-button v-size-width v-font-size"
                                  style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #140173; background-color: #f99d05; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:31%; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 14px;">
                                  <span style="display:block;padding:10px 20px;line-height:120%;"><span
                                      style="line-height: 16.8px;">Register Now</span></span>
                                </a>
                                <!--[if mso]></center></v:roundrect><![endif]-->
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_text_3" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px 131px 60px 50px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <div class="v-text-align v-font-size"
                                style="font-size: 12px; color: #95a5a6; line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="line-height: 140%;">Thank you </p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div><!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>





          <div class="u-row-container" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #ffffff;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                  <div
                    style="background-color: #ffffff;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div
                      style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--<![endif]-->

                      <table id="u_content_heading_2" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:40px 10px 10px 35px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <!--[if mso]><table width="100%"><tr><td><![endif]-->
                              <h1 class="v-text-align v-font-size"
                                style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-size: 22px; font-weight: 400;">
                                <span><span><span
                                      data-metadata="&lt;!--(figmeta)eyJmaWxlS2V5IjoiMlBQSXNjNFd3Q2ZlU0tINFZVMlBXeiIsInBhc3RlSUQiOjk3MDc2NDM4NywiZGF0YVR5cGUiOiJzY2VuZSJ9Cg==(/figmeta)--&gt;"></span><span
                                      data-buffer="&lt;!--(figma)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(/figma)--&gt;"></span><span>Thanks
                                      for the support! 😍</span></span></span></h1>
                              <!--[if mso]></td></tr></table><![endif]-->

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px 35px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #d3d3d3;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <tbody>
                                  <tr style="vertical-align: top">
                                    <td
                                      style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                      <span>&#160;</span>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_social_1" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 10px 35px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <div align="left">
                                <div style="display: table; max-width:83px;">
                                  <!--[if (mso)|(IE)]><table width="83" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="left"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:83px;"><tr><![endif]-->


                                  <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 10px;" valign="top"><![endif]-->
                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32"
                                    style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 10px">
                                    <tbody>
                                      <tr style="vertical-align: top">
                                        <td align="left" valign="middle"
                                          style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                          <a href="https://www.instagram.com/chiragjoshi.07/" title="Instagram"
                                            target="_blank">
                                            <img src="images/image-3.png" alt="Instagram" title="Instagram" width="32"
                                              style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  <!--[if (mso)|(IE)]></td><![endif]-->

                                  <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32"
                                    style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
                                    <tbody>
                                      <tr style="vertical-align: top">
                                        <td align="left" valign="middle"
                                          style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                          <a href="https://github.com/Chiragj2003" title="GitHub" target="_blank">
                                            <img src="images/image-2.png" alt="GitHub" title="GitHub" width="32"
                                              style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  <!--[if (mso)|(IE)]></td><![endif]-->


                                  <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                                </div>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div><!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>



          <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
      </tr>
    </tbody>
  </table>
  <!--[if mso]></div><![endif]-->
  <!--[if IE]></div><![endif]-->
</body>

</html>
    """

    # Send email with OTP
    send_email(receiver_email, html_content)

    # Check OTP
    otp_checker(otp)

if __name__ == "__main__":
    main()
