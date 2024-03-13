#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  let xvar = 0;
  while (xvar <= list.length) {
	  if (list[xvar] === searchElement) {
		  nOccurrences++;
	  }
	  xvar++;
  }
  return nOccurrences;
};
