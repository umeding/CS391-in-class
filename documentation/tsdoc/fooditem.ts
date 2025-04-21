/**
 * Represents a food item.
 *
 * @remarks This class is used to store information about food items.
 */
class Foodtem {
  /**
   * The name of the food item.
   */
  name: string;

  /**
   * The details for the food item.
   */
  details: string;

  /**
   * Creates a new instance of the `Foodtem` class.
   *
   * @param name - The name of the food item.
   * @param details - The details for the food item.
   */
  constructor(name: string, details: string) {
    this.name = name;
    this.details = details;
  }

  /**
   * Get the description for the food item.
   *
   * @returns The food item description.
   */
  getDescription(): string {
    return `${this.name} -- ${this.details}`;
  }
}

// Create a new food item instance
const myFoodtem = new Foodtem('Pizza', 'Tomato, Basil, Cheese');

// Get the food item description
console.log(myFoodtem.getDescription()); // Output: "Pizza -- Tomato, Basil, Cheese"

