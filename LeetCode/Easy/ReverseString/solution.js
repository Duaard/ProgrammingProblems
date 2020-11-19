/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    // Loop half of array
    for(let i = 0; i < s.length/2; i++) {
        // Get the inverse index of i
        let j = s.length -1 - i;
        // Swap i and j
        [s[i], s[j]] = [s[j], s[i]];
    }
};