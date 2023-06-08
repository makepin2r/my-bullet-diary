const clickInputData = () => {
  let todo = document.getElementById("todo_input").value;
  let selc = document.getElementById("input_select").value;

  let formData = new FormData();
  formData.append("todo_give", bucket);
  formData.append("selc_give", bucket);

  console.log(todo, selc);
  fetch("/inputData", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
};
