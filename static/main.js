const imageInput = document.getElementById("imageInput");

const processButton = document.getElementById("processButton");

const originalImage = document.getElementById("originalImage");

const resultImage = document.getElementById("resultImage");

imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if (!file) return;

    originalImage.src = URL.createObjectURL(file);

});

processButton.addEventListener("click", async () => {

    const file = imageInput.files[0];

    if (!file) {

        alert("Выберите изображение");

        return;

    }

    const formData = new FormData();

    formData.append("image", file);

    const response = await fetch("/process", {

        method: "POST",

        body: formData

    });

    const data = await response.json();

    resultImage.src = data.image + "?" + Date.now();

    document.getElementById("count").innerText = data.count;

    document.getElementById("area").innerText = data.area + " %";

    document.getElementById("time").innerText = data.time + " сек";

});