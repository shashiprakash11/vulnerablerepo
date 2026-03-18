const name = new URLSearchParams(window.location.search).get("name");
document.body.innerHTML = "Hello " + name;
