/**
 * Represents a food item.
 * @constructor
 * @param {string} name - The name of the food item.
 * @param {string} details - The details for the food item.
 */
function FoodItem(name, details)   
 {
  /**
   * @member {string}
   */
  this.name = name;
  /**
   * @member {string}
   */
  this.details = details;

  /**
   * Get the description of the food item.
   * @return {string} The food item description.
   */
  this.getDescription = function() {
    return this.name + ' -- ' + this.details;
  };
}

// Create a new food item instance
const myPizza = new FoodItem('Pizza', 'Tomato, Basil, Cheese');

// Get the food item description
console.log(myPizza.getDescription()); // Output: "Pizza -- Tomato, Basil, Cheese"
