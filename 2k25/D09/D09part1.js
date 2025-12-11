async function findPart1(points){
    let maxSize = 0
    for (let idx1 = 0; idx1 < points.length; idx1++){

        let [x,y] = points[idx1]
        drawPoint([x,y])

        for (let idx2 = idx1; idx2 < points.length; idx2++){
    
            const [x1,y1] = points[idx1]
            const [x2,y2] = points[idx2]
            const size = (Math.abs(x1-x2)+1)*(Math.abs(y1-y2)+1)

            if (size > maxSize){
                maxSize = size
                displayPart1.innerText = maxSize
                cleanCanvas(1)
                drawArea([x1,y1],[x2,y2],"#f00","ff000010",1)
            }
        }
    }

    return maxSize
}

async function part1(points){

    ctxArr[0].clearRect(0,0,canvasArr[0].width, canvasArr[0].height);
    ctxArr[1].clearRect(0,0,canvasArr[0].width, canvasArr[0].height);
    ctxArr[2].clearRect(0,0,canvasArr[0].width, canvasArr[0].height);

    ctxArr[0].fillStyle = "#f00"
    ctxArr[1].fillStyle = "#ff000010"
    ctxArr[1].strokeStyle = "#f00"

    for(let idx=0;idx<points.length;idx++){
        ctxArr[0].clearRect(0,0,canvasArr[0].width, canvasArr[0].height)
        await findPart1(points.slice(0,idx))
        if(SLEEP_T) await new Promise(r => setTimeout(r, SLEEP_T));
    }

    cleanCanvas(1)

}