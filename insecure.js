const userInput = process.argv[2];

// ❌ Code Injection
eval(userInput);
