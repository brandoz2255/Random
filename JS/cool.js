


//simulates the enum in C++ so this is similar to what an enum is in C++
const ConversionType = {
    InchesToCentimeters: 0,
    CentimetersToInches: 1,
    OuncesToGrams: 2,
    GramsToOunces: 3,
    MilesToKilometers: 4,
    KilometersToMiles: 5,
    CelsiusToFahrenheit: 6
};


//user greeting function that displays a user greeting in JS
function userGreeting() {
    console.log("\033[1;32m");
    console.log(`
   .____      _____ __________  ____________  ._._. 
 |   |    / _ \\______  \\ /_  \\_____ \\ | | | 
 |   |   / /_\\ \\|   | _/ |  | _(__ < | | | 
 |   |___/   |   \\   |  \\ |  |/      \\ \\|\| 
 |_______ \\____|__ /______ / |___/______ / ____ 
        \\/      \\/      \\/             \\/  \\/\/ 
    `);
    console.log("\033[0m");
    console.log("Hello and welcome to this program!");
    console.log("\033[1;32m---------------------------------------------------");
    console.log("\033[1;93mEssentially, this program will allow you to do conversions in multiple fields\033[1;32m");
    console.log("---------------------------------------------------");
 }

 //does the conversion so that you dont have to asks the user for the input and goes through a control flow on the users input
 function getConversionType() {
    let message = prompt("\033[1;32mPlease input the following to use this program for conversion.\033[0m" +
    "\n'I' Will convert Inches to Centimeters." +
    "\n'C' Will convert Centimeters to Inches." +
    "\n'O' Will convert Ounces to Grams." +
    "\n'G' Will convert from Grams to Ounces." +
    "\n'M' Will convert from Miles to Kilometers." +
    "\n'K' Will convert Kilometers to miles." +
    "\n'T' Will convert Celsius to Fahrenheit.");
    if (message === "I" || message === "i") {
        return ConversionType.InchesToCentimeters;
    } else if (message === "C" || message === "c") {
        return ConversionType.CentimetersToInches;
    } else if (message === "O" || message === "o") {
        return ConversionType.OuncesToGrams;
    } else if (message === "G" || message === "g") {
        return ConversionType.GramsToOunces;
    } else if (message === "M" || message === "m") {
        return ConversionType.MilesToKilometers;
    } else if (message === "K" || message === "k") {
        return ConversionType.KilometersToMiles;
    } else if (message === "T" || message === "t") {
        return ConversionType.CelsiusToFahrenheit;
    }
    alert("I'm sorry, I did not understand the value. Please type the correct value.");
    return null;
 }



//user greeting function that displays a user greeting in JS
function userGreeting() {
    console.log("\033[1;32m");
    console.log(`
   .____      _____ __________  ____________  ._._. 
 |   |    / _ \\______  \\ /_  \\_____ \\ | | | 
 |   |   / /_\\ \\|   | _/ |  | _(__ < | | | 
 |   |___/   |   \\   |  \\ |  |/      \\ \\|\| 
 |_______ \\____|__ /______ / |___/______ / ____ 
        \\/      \\/      \\/             \\/  \\/\/ 
    `);
    console.log("\033[0m");
    console.log("Hello and welcome to this program!");
    console.log("\033[1;32m---------------------------------------------------");
    console.log("\033[1;93mEssentially, this program will allow you to do conversions in multiple fields\033[1;32m");
    console.log("---------------------------------------------------");
 }

 function getConversionType() {
    let message = prompt("\033[1;32mPlease input the following to use this program for conversion.\033[0m" +
    "\n'I' Will convert Inches to Centimeters." +
    "\n'C' Will convert Centimeters to Inches." +
    "\n'O' Will convert Ounces to Grams." +
    "\n'G' Will convert from Grams to Ounces." +
    "\n'M' Will convert from Miles to Kilometers." +
    "\n'K' Will convert Kilometers to miles." +
    "\n'T' Will convert Celsius to Fahrenheit.");
    if (message === "I" || message === "i") {
        return ConversionType.InchesToCentimeters;
    } else if (message === "C" || message === "c") {
        return ConversionType.CentimetersToInches;
    } else if (message === "O" || message === "o") {
        return ConversionType.OuncesToGrams;
    } else if (message === "G" || message === "g") {
        return ConversionType.GramsToOunces;
    } else if (message === "M" || message === "m") {
        return ConversionType.MilesToKilometers;
    } else if (message === "K" || message === "k") {
        return ConversionType.KilometersToMiles;
    } else if (message === "T" || message === "t") {
        return ConversionType.CelsiusToFahrenheit;
    }
    alert("I'm sorry, I did not understand the value. Please type the correct value.");
    return null;
 }

 
 function calculateAndDisplay(conversionType) {
    if (conversionType === ConversionType.CelsiusToFahrenheit) {
        // Implement the Celsius to Fahrenheit conversion here
    } else {
        let number = parseFloat(prompt("\nPlease enter an integer: "));
        let math;
        switch (conversionType) {
            case ConversionType.InchesToCentimeters:
                math = number * 2.54;
                console.log(`\n${number}\nInches Equals\n${math}\nCentimeters`);
                break;
            case ConversionType.CentimetersToInches:
                math = number * 0.3937;
                console.log(`\n${number}\nCentimeters Equals\n${math}\nInches`);
                break;
            case ConversionType.OuncesToGrams:
                math = number * 28.34952;
                console.log(`\n${number}\nOunces Equals\n${math}\nGrams`);
                break;
            case ConversionType.GramsToOunces:
                math = number / 28.34952;
                console.log(`\n${number}\nGrams Equals\n${math}\nOunces`);
                break;
            case ConversionType.MilesToKilometers:
                math = number * 1.609344;
                console.log(`\n${number}\nMiles Equals\n${math}\nKilometers`);
                break;
            case ConversionType.KilometersToMiles:
                math = number * 0.621371;
                console.log(`\n${number}\nKilometers Equals\n${math}\nMiles```
        } 
    }
 }

function askToContinue() {
    console.log("\033[1;32m---------------------------------------------------"); 
   
    let answer = prompt("Would you like to use this program again [Y/N]: ");

    if(answer === 'Y' || answer === 'y'){
        return true;
    } else if (answer === 'N' || answer === 'n'){
        return false
    }else {
        console.log("\033[1;32m--------------------------------------------------------")
        console.log("did not understand you input please enter either or [n/y]")
    }

}

function exitMessage(){
    console.log("\033[1;32m--------------------------------------------------------")
    console.log("\033[1;32m----------------------------ok---------------------------")
    console.log("\033[1;32m--------------------------------------------------------")

}

userGreeting();
let conversionTypeMain = getConversionType();
if (conversionTypeMain !== null) {
    calculateAndDisplay(conversionTypeMain);
    let runMainProgram = askToContinue();
    while (runMainProgram) {
        userGreeting();
        conversionTypeMain = getConversionType();
        if (conversionTypeMain !== null) {
            calculateAndDisplay(conversionTypeMain);
            runMainProgram = askToContinue();
        }
    }
}
exitMessage();

 // does the calculations of the user input based on the control flow mentioned earlier  in this case uses on the else statement uses a swithc case
 function calculateAndDisplay(conversionType) {
    if (conversionType === ConversionType.CelsiusToFahrenheit) {
        // Implement the Celsius to Fahrenheit conversion here
    } else {
        let number = parseFloat(prompt("\nPlease enter an integer: "));
        let math;
        switch (conversionType) {
            case ConversionType.InchesToCentimeters:
                math = number * 2.54;
                console.log(`\n${number}\nInches Equals\n${math}\nCentimeters`);
                break;
            case ConversionType.CentimetersToInches:
                math = number * 0.3937;
                console.log(`\n${number}\nCentimeters Equals\n${math}\nInches`);
                break;
            case ConversionType.OuncesToGrams:
                math = number * 28.34952;
                console.log(`\n${number}\nOunces Equals\n${math}\nGrams`);
                break;
            case ConversionType.GramsToOunces:
                math = number / 28.34952;
                console.log(`\n${number}\nGrams Equals\n${math}\nOunces`);
                break;
            case ConversionType.MilesToKilometers:
                math = number * 1.609344;
                console.log(`\n${number}\nMiles Equals\n${math}\nKilometers`);
                break;
            case ConversionType.KilometersToMiles:
                math = number * 0.621371;
                console.log(`\n${number}\nKilometers Equals\n${math}\nMiles```
        } 
    }
 }

 // asks the user is they should continue the program using the prompt() method and puts a controil flow based on the users input
function askToContinue() {
    console.log("\033[1;32m---------------------------------------------------"); 
   
    let answer = prompt("Would you like to use this program again [Y/N]: ");

    if(answer === 'Y' || answer === 'y'){
        return true;
    } else if (answer === 'N' || answer === 'n'){
        return false
    }else {
        console.log("\033[1;32m--------------------------------------------------------")
        console.log("did not understand you input please enter either or [n/y]")
    }

}

// exits message simple just prints it out 
function exitMessage(){
    console.log("\033[1;32m--------------------------------------------------------")
    console.log("\033[1;32m----------------------------ok---------------------------")
    console.log("\033[1;32m--------------------------------------------------------")

}

// main function of the code 
userGreeting();
let conversionTypeMain = getConversionType();
if (conversionTypeMain !== null) {
    calculateAndDisplay(conversionTypeMain);
    let runMainProgram = askToContinue();
    while (runMainProgram) {
        userGreeting();
        conversionTypeMain = getConversionType();
        if (conversionTypeMain !== null) {
            calculateAndDisplay(conversionTypeMain);
            runMainProgram = askToContinue();
        }
    }
}
exitMessage();





