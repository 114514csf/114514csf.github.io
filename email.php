<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 获取表单字段
    $name = isset($_POST['name']) ? htmlspecialchars(trim($_POST['name'])) : '';
    $email = isset($_POST['email']) ? htmlspecialchars(trim($_POST['email'])) : '';
    $message = isset($_POST['message']) ? htmlspecialchars(trim($_POST['message'])) : '';

    // 邮件收件人
    $to = "F114514CS@outlook.com"; // 请将此处替换为你的邮箱

    // 邮件主题
    $subject = "表单新消息来自: $name";

    // 邮件内容
    $body = "姓名: $name\n";
    $body .= "邮箱: $email\n";
    $body .= "内容:\n$message\n";

    // 邮件头部
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    // 发送邮件
    if (mail($to, $subject, $body, $headers)) {
        echo "邮件发送成功！";
    } else {
        echo "邮件发送失败，请稍后重试。";
    }
} else {

}
?>
