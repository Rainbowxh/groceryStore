function deepTravel(node, nodelist) {
  if (node === null) {
    return;
  }
  nodelist.push(node);
  let children = node.children;
  for (let i = 0; i < children.length; i++) {
    deepTravel(children[i], nodelist);
  }
  return nodelist;
}
function deepTravel2(node) {
  let nodes = [];
  if (node === null) {
    return;
  }
  nodes.push(node);
  let children = node.children;
  for (let i = 0; i < children.length; i++) {
    nodes = nodes.contact(deepTravel(children[i]));
  }
  return nodes;
}

function deepTravel3(node) {
  let nodes = [];
  let stack = [];
  if (node === null) {
    return;
  }
  stack.push(node);
  while (stack.length) {
    let item = stack.pop();
    let children = item.children;
    node.push(item);
    for (let i = children.length - 1; i >= 0; i--) {
      stack.push(children[i]);
    }
  }
}

function widthTravel(node) {
  let nodes = [];
  let stack = [];
  if (node == null) {
    return;
  }
  stack.push(node)
  while (stack.length){
      let item = stack.shift()
      let children = item.children
      nodes.push(item)
      for ( let i =0 ; i< children.length;i++){
          stack.push(children[i])
      }
  }
}
