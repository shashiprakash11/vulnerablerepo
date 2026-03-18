// XSS
document.body.innerHTML = location.search;

// Prototype Pollution
let obj = {};
obj[location.hash.substring(1)] = "polluted";

// Eval injection
eval(location.search);
