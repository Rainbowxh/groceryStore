// Loop through our chapter urls
story.chapterUrls.reduce(function(sequence, chapterUrl) {
  // Add these actions to the end of the sequence
  return sequence
    .then(function() {
      return getJSON(chapterUrl);
    })
    .then(function(chapter) {
      addHtmlToPage(chapter.html);
    });
}, Promise.resolve());

var arr = ["a", "b", "c", "d", "e", "f", "g"];
var result = [];
var sequence = Promise.resolve();

arr.map(ele => {
  setTimeout(() => {
    console.log(ele);
    setTimeout(() => {
      console.log(arr.indexOf(ele));
    }, 1000 * arr.indexOf(ele));
  }, 3000 * arr.indexOf(ele));
});
arr.forEach(function(item, index) {
  setTimeout(() => {
    console.log(item);
    setTimeout(() => {
      console.log(arr.indexOf(item));
    }, 1000 * arr.indexOf(item));
  }, 3000 * arr.indexOf(item));
});
console.log(result);

for (let i = 0; i < 8; i++) {
  setInterval(() => {
    console.log(this);
  }, 2000);
}

arr.forEach(function(item, index) {
  let self = this;
  sequence = sequence.then(() => {
    this.result.push(item);
  });
});
arr.map(ele => {
  return this.sequence.then(function() {
    setTimeout(() => {
      console.log(ele);
      setTimeout(() => {
        console.log(arr.indexOf(ele));
      }, 1000 * arr.indexOf(ele));
    }, 3000 * arr.indexOf(ele));
  });
});
console.log(result);

function IteratorInstance(items) {
  let i = 0;
  return {
    next: function() {
      let done = i >= items.length;
      let value = !done ? items[i++] : undefined;
      return {
        value: value,
        done: done
      };
    }
  };
}

let iterator = IteratorInstance(arr);
iterator.next();
iterator.next();
iterator.next();
iterator.next();

function* createGenerator() {
  for (let i = 0; i < 10; i++) {
    yield i;
  }
}
console.log(createGenerator.next());
console.log(createGenerator.next());
console.log(createGenerator.next());
