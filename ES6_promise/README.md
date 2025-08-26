# Web Backend - ES6 Promises
## This directory contains task files for the ES6 Promises project.

0-promise.js - Returns a Promise using this prototype function getResponseFromAPI().

1-promise.js - Returns a promise.

2-then.js - Append three handlers to the function.

3-all.js - Return promises, use the prototype below to collectively resolve all promises and log body firstName lastName to the console.

4-user-promise.js - Returns a resolved promise with given object.

5-photo-reject.js - Contains a function named uploadPhoto. It should accept one argument fileName (string). The function should return a Promise rejecting with an Error and the string $fileName cannot be processed.

6-final-user.js - Contains a function named handleProfileSignup. It should accept three arguments firstName (string), lastName (string), and fileName (string). The function should call the two other functions. When the promises are all settled it should return an array.

7-load_balancer.js - Contains  function named loadBalancer. It should accept two arguments chinaDownload (Promise) and USDownload (Promise).
The function should return the value returned by the promise that resolved the first.

8-try.js - Contains a function named divideFunction that will accept two arguments: numerator (Number) and denominator (Number).
When the denominator argument is equal to 0, the function should throw a new error with the message cannot divide by 0. Otherwise it should return the numerator divided by the denominator.

9-try.js - Contains  a function named guardrail that will accept one argument mathFunction (Function).
This function should create and return an array named queue.
