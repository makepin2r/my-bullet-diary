function login() {
    let id = $('#loginID').val()
    let pw = $('#loginPW').val()

    let formData = new FormData();
    formData.append("id_give", id);
    formData.append("pw_give", pw);

    fetch("/login", { method: "GET", body: formData })
        .then((res) => res.json())
        .then((data) => {
            console.log(result)
            //window.location.reload()
    });
}