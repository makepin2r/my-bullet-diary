$(document).ready(function () {
  show_list();
});
function show_list() {
  $("#Todo-list").empty;
  fetch("/list")
    .then((res) => res.json())
    .then((data) => {
      let rows = data["result"];
      rows.forEach((a) => {
        let todo = a["list"];
        let num = a["num"];
        let isChecked = a["isChecked"];
        let focused = a["focused"];

        let temp_html = ``;
        if (isChecked === 0) {
          temp_html = `<h5 class='temp'>
                                        <input class="form-check-input" onclick='check(${isChecked})' type="checkbox" id="checkboxNoLabel">
                                        <i class="bi bi-star" onclick="focusing(${focused})" id="star"></i>
                                        <p class='today'>${todo}</p>
                                        <i class="bi1 bi-trash3" onclick="del(${num})" ></i>
                                    </h5>`;
        } else {
          temp_html = `<h5 class='temp'>
                                        <p class='today'>${todo} 완료!</p>
                                        <i class="bi1 bi-trash3" onclick="del(${num})" ></i>
                                    </h5>`;
        }
        $("#Todo-list").append(temp_html);
      });
    });
}

function del(num) {
  let formData = new FormData();
  formData.append("num_give", num);

  fetch("/list/delete", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
function save_list() {
  let list = $("#input_box").val();

  let formData = new FormData();
  formData.append("list_give", list);

  fetch("/list", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
function check(isChecked) {
  let formData = new FormData();
  formData.append("check_give", isChecked);

  fetch("/list/isChecked", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
function focusing(focused) {
  let formData = new FormData();
  formData.append("focused_give", focused);

  fetch("/list/focused", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
