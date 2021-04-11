const ctx = div.getContext("2d");
div.width = 500;
div.height = 500;
const rand = (m = 255, M = m + (m = 0)) => (Math.random() * (M - m) + m) | 0;


const objects = [];
for (let i = 0; i < 100; i++) {
  objects.push({x: rand(div.width), y: rand(div.height),w: rand(40),h: rand(40), col: `rgb(${rand()},${rand()},${rand()})`});
}

requestAnimationFrame(drawdiv);

const view = (() => {
  const matrix = [1, 0, 0, 1, 0, 0]; // current view transform
  var m = matrix;             // alias
  var scale = 1;              // current scale
  var ctx;                    // reference to the 2D context
  const pos = { x: 0, y: 0 }; // current position of origin
  var dirty = true;
  const API = {
    set context(_ctx) { ctx = _ctx; dirty = true },
    apply() {
      if (dirty) { this.update() }
      ctx.setTransform(m[0], m[1], m[2], m[3], m[4], m[5])
    },
    get scale() { return scale },
    get position() { return pos },
    isDirty() { return dirty },
    update() {
      dirty = false;
      m[3] = m[0] = scale;
      m[2] = m[1] = 0;
      m[4] = pos.x;
      m[5] = pos.y;
    },
    pan(amount) {
      if (dirty) { this.update() }
       pos.x += amount.x;
       pos.y += amount.y;
       dirty = true;
    },
    scaleAt(at, amount) { // at in screen coords
      if (dirty) { this.update() }
      scale *= amount;
      pos.x = at.x - (at.x - pos.x) * amount;
      pos.y = at.y - (at.y - pos.y) * amount;
      dirty = true;
    },
  };
  return API;
})();
view.context = ctx;
function drawdiv() {
    if (view.isDirty()) {
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, div.width, div.height);

        view.apply(); // set the 2D context transform to the view
        for (i = 0; i < objects.length; i++) {
            var obj = objects[i];
            ctx.fillStyle = obj.col;
            ctx.fillRect(obj.x, obj.y, obj.h, obj.h);
        }
    }
    requestAnimationFrame(drawdiv);
}


div.addEventListener("mousemove", mouseEvent, {passive: true});
div.addEventListener("mousedown", mouseEvent, {passive: true});
div.addEventListener("mouseup", mouseEvent, {passive: true});
div.addEventListener("mouseout", mouseEvent, {passive: true});
div.addEventListener("wheel", mouseWheelEvent, {passive: false});
const mouse = {x: 0, y: 0, oldX: 0, oldY: 0, button: false};
function mouseEvent(event) {
    if (event.type === "mousedown") { mouse.button = true }
    if (event.type === "mouseup" || event.type === "mouseout") { mouse.button = false }
    mouse.oldX = mouse.x;
    mouse.oldY = mouse.y;
    mouse.x = event.offsetX;
    mouse.y = event.offsetY
    if(mouse.button) { // pan
        view.pan({x: mouse.x - mouse.oldX, y: mouse.y - mouse.oldY});
    }
}
function mouseWheelEvent(event) {
    var x = event.offsetX;
    var y = event.offsetY;
    if (event.deltaY < 0) { view.scaleAt({x, y}, 1.1) }
    else { view.scaleAt({x, y}, 1 / 1.1) }
    event.preventDefault();
}
