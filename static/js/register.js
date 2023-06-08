function register() {
    $.ajax({
        type: "POST",
        url: "/api/register",
        data: {
            id_give: $("#userID").val(),
            pw_give: $("#userPW2").val(),
            nickname_give: $("#nickname").val(),
        },
        success: function (response) {
            if (response["result"] == "success") {
                alert("회원가입이 완료되었습니다.");
                window.location.href = "/login";
            } else {
                alert(response["msg"]);
            }
        },
    });
}

// 비밀번호 입력 1차 & 2차 동일한지 확인
function comparePW(){
    if($("userPW1").val() == $("userPW2").val()){
        $('#pwMessage2').text("비밀번호가 일치합니다")
    } else {
        $('#pwMessage2').text("비밀번호가 일치하지 않습니다")
    }
}

// 비밀번호가 규칙(영문 소문자,숫자만 사용 8~15자)에 맞는지 확인
// 인풋에 입력 들어올 때마다 호출
function validatePW(){
    const target = $("#userPW1").val()
    console.log(target)
    const reg = '/^(?=.*[a-zA-Z])(?=.*[0-9]).{8,15}$/'
    if(target.test(reg)){
        $('#pwMessage1').text("사용 가능한 비밀번호입니다")
    } else {
        $('#pwMessage1').text("영문 소문자, 숫자가 포함된 8~15자의 비밀번호를 입력해주세요")
    }
}