function login() {
    let id = $('#idForm').val()
    let pw = $('#pwForm').val()

    let formData = new FormData();
    formData.append("id_give", name);
    formData.append("pw_give", comment);

    fetch("/login", { method: "POST", body: formData })
        .then((res) => res.json())
        .then((data) => {
            console.log(result)
            //window.location.reload()
    });
}