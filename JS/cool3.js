


const readline = require('readline');

const ConversionType = {
    InchesToCentimeters: 0,
    CentimetersToInches: 1,
    OuncesToGrams: 2,
    GramsToOunces: 3,
    MilesToKilometers: 4,
    KilometersToMiles: 5,
    CelsiusToFahrenheit: 6
};

//This function prints a welcome message to the console. It uses escape sequences to print colored text.
function userGreeting() {
    console.log("\x1b[1;32m");
    console.log(`
   .____      _____ __________  ____________  ._._.
 |   |    / _ \\______  \\ /_  \\_____ \\ | | |
 |   |   / /_\\ \\|   | _/ |  | _(__ < | | |
 |   |___/   |   \\   |  \\ |  |/      \\ \\|\\|
 |_______ \\____|__ /______ / |___/______ / ____
        \\/      \\/      \\/             \\/  \\\\/
    `);
    console.log("\x1b[0m");
    console.log("Hello and welcome to this program!");
    console.log("\x1b[1;32m---------------------------------------------------");
    console.log("\x1b[1;93mEssentially, this program will allow you to do conversions in multiple fields\x1b[1;32m");
    console.log("---------------------------------------------------");
}

//This function asks the user to select a conversion type. It uses the readline module to get user input. The function returns a promise that resolves to the chosen conversion type.
function getConversionType() {
    //creates the readline interface 
    return new Promise((resolve) => {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

    // Use readline.question() to prompt the user for input
   // This function takes a string (the prompt) and a callback function
   // The callback function is executed when the user provides input

        rl.question("\x1b[1;32mPlease input the following to use this program for conversion.\x1b[0m" +
            "\n'I' Will convert Inches to Centimeters." +
            "\n'C' Will convert Centimeters to Inches." +
            "\n'O' Will convert Ounces to Grams." +
            "\n'G' Will convert from Grams to Ounces." +
            "\n'M' Will convert from Miles to Kilometers." +
            "\n'K' Will convert Kilometers to miles." +
            "\n'T' Will convert Celsius to Fahrenheit: ", (answer) => {
                // close the parenthesis interface after getting the user input 
                rl.close();

                switch (answer.toLowerCase()) {
                    case 'i':
                        resolve(ConversionType.InchesToCentimeters);
                        break;
                    case 'c':
                        resolve(ConversionType.CentimetersToInches);
                        break;
                    case 'o':
                        resolve(ConversionType.OuncesToGrams);
                        break;
                    case 'g':
                        resolve(ConversionType.GramsToOunces);
                        break;
                    case 'm':
                        resolve(ConversionType.MilesToKilometers);
                        break;
                    case 'k':
                        resolve(ConversionType.KilometersToMiles);
                        break;
                    case 't':
                        resolve(ConversionType.CelsiusToFahrenheit);
                        break;
                    default:
                        console.log("I'm sorry, I did not understand the value. Please type a valid option.");
                        resolve(null);
                }
            });
    });
}

//This function asks the user whether they want to continue using the program. Like getConversionType(), it uses the readline module to get user input and returns a promise that resolves to a boolean value indicating whether the user wants to continue.
function askToContinue() {
    return new Promise((resolve) => {
        console.log("\x1b[\n1;32m---------------------------------------------------");
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
 // Resolve the promise with a boolean value based on the user's input
        rl.question("\nWould you like to use this program again [Y/N]: \n", (answer) => {
            rl.close();
            resolve(answer.toLowerCase() === 'y');
        });
    });
}

//calculates and displays the shit the covnersions using a control flow of the switch statements
function calculateAndDisplay(conversionType) {
    return new Promise((resolve) => {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
 
        rl.question("\nPlease enter a number --> ", (inputNumber) => {
            rl.close();
 
            const number = parseFloat(inputNumber);
 
            if (isNaN(number)) {
                console.log("Invalid input. Please enter a valid number.");
                resolve();
                return;
            }
 
            let result;
 
            switch (conversionType) {
                case ConversionType.InchesToCentimeters:
                   result = number * 2.54;
                   console.log(`\n${number} Inches Equals ${result} Centimeters`);
                   break;
                case ConversionType.CentimetersToInches:
                   result = number * 0.3937;
                   console.log(`\n${number} Centimeters Equals ${result} Inches`);
                   break;
                case ConversionType.OuncesToGrams:
                   result = number * 28.34952;
                   console.log(`\n${number} Ounces Equals ${result} Grams`);
                   break;
                case ConversionType.GramsToOunces:
                   result = number / 28.34952;
                   console.log(`\n${number} Grams Equals ${result} Ounces`);
                   break;
                case ConversionType.MilesToKilometers:
                   result = number * 1.609344;
                   console.log(`\n${number} Miles Equals ${result} Kilometers`);
                   break;
                case ConversionType.KilometersToMiles:
                   result = number * 0.621371;
                   console.log(`\n${number} Kilometers Equals ${result} Miles`);
                   break;
            }
 
            resolve();
        });
    });
 }
 
//This function prints a goodbye message to the console.
function exitMessage() {
    console.log("\x1b[1;32m--------------------------------------------------------");
    console.log("\x1b[1;32m----------------------------OK---------------------------");
    console.log("\x1b[1;32m--------------------------------------------------------");
}

//This is the main function of the program. It runs a loop that continues until the user decides to stop. Inside the loop, it calls all the other functions in the correct order and waits for each one to finish before moving on to the next.
async function runProgram() {
    let runMainProgram = true;

    while (runMainProgram) {
        await userGreeting();
        let conversionTypeMain = await getConversionType();

        if (conversionTypeMain !== null) {
            await calculateAndDisplay(conversionTypeMain);
            runMainProgram = await askToContinue();
        } else {
            runMainProgram = false; // Exit if conversion type is null
        }
    }

    exitMessage();
}


runProgram();

//Remember, when working with the readline module in Node.js, it's important to close the readline interface after you're done using it.
