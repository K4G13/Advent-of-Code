// Nodes' refs
const displayPart1 = document.getElementById("display-part-1")
const displayPart2 = document.getElementById("display-part-2")
const canvasArr = document.getElementsByTagName("canvas")

// Canvas paint params
let ctxArr = []
let scale

async function loadPoints(filePath) {
    const response = await fetch(filePath)
    const text = await response.text()

    const points = text
        .trim()
        .split("\n")
        .map(line=>line.split(",").map(Number))

    return points
}

function setUpCanvases(points){

    let canvasSize = 0
    for(c of canvasArr) 
        canvasSize = Math.max(c.height,c.width,canvasSize)
    for(c of canvasArr){
        c.height = canvasSize
        c.width = canvasSize
        ctxArr.push(c.getContext("2d"))
    }
    
    maxX = 0, maxY = 0
    for([x,y] of points){
        maxX = Math.max(maxX,x)
        maxY = Math.max(maxY,y)
    }

    scale = canvasSize / Math.max(maxX+2,maxY+2)
}

function cleanCanvas(ctxIdx=0){
    ctxArr[ctxIdx].clearRect(0,0,canvasArr[ctxIdx].width, canvasArr[ctxIdx].height);
}

function drawPoint([x,y],color="red",ctxIdx=0,size=1){
    ctxArr[ctxIdx].fillStyle = color
    ctxArr[ctxIdx].fillRect(x*scale - size/2,y*scale - size/2,size,size)
}

function drawArea([x1,y1],[x2,y2],stroke="#ff0000",fill="#ff000010",ctxIdx=0){

    ctxArr[ctxIdx].strokeStyle = stroke
    ctxArr[ctxIdx].fillStyle = fill
    ctxArr[ctxIdx].beginPath()
    ctxArr[ctxIdx].moveTo(x1*scale,y1*scale)
    ctxArr[ctxIdx].lineTo(x1*scale,y2*scale)
    ctxArr[ctxIdx].lineTo(x2*scale,y2*scale)
    ctxArr[ctxIdx].lineTo(x2*scale,y1*scale)
    ctxArr[ctxIdx].lineTo(x1*scale,y1*scale)
    ctxArr[ctxIdx].stroke()
    ctxArr[ctxIdx].fill()

}
