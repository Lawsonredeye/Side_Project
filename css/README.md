# Learning CSS with W3SCHOOL

## Selectors:

these are used for finding and styling html elements with special properties and values.

it works in this syntax:
selector {
property: value; property: value;
}

each selectors property and value are separated by semi-colons and a selector can contain multiple properties and values.

A css rule is formed by a selector (which targets html elements), property(which defines what the style would be applied) and value (which is the value of the property).

### Grouping

Grouping is necessary for targeting elements that has similar properties and values. This helps in keeping codes DRY(dont, repeat yourself). For instance;

p {
font-family: monospace;
font-size: 20px;
}

h1 {
font-family: monospace;
font-size: 20px;
}

h2 {
font-family: monospace;
font-size: 20px;
}

It could also be written as:
p, h1, h2 {
font-family: monospace;
font-size: 20px;
}

This would make each elements to have the same property and value even tho the elements are different.

## Types of Selectors

1. ID selector: uses the id attributes to target html element which has the pound (#) symbol
2. class selector: this targets element that has the class attributes and its denoted by the dot (.) symbol
3. universal selector: This acts as a wildcard to target every HTML elements and its denoted by the asterick (\*) symbol

## Resources

Here are the resources used for learning css

1. [w3schools](https://www.w3schools.com/css)
