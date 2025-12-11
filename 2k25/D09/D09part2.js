async function drawPoints(points){
    for(A of points){
        for(B of points)
            drawPoint(A,"red",0,1)
        if(SLEEP_T) await new Promise(r => setTimeout(r, SLEEP_T));
    }
}

async function connectPoints(points) {

    canvasId = 2

    ctxArr[canvasId].strokeStyle = "#00ff00"
    ctxArr[canvasId].fillStyle = "#00ff0010"
    
    for(let i=0;i<points.length;i++){

        cleanCanvas(canvasId)
        ctxArr[canvasId].beginPath()
        ctxArr[canvasId].moveTo(points[0][0]*scale,points[0][1]*scale)

        for(let idx=0;idx<i;idx++){
            curr = points[idx]
            next = points[(idx+1)%points.length]
            ctxArr[canvasId].lineTo(next[0]*scale,next[1]*scale)
        }  
        ctxArr[canvasId].lineTo(points[0][0]*scale,points[0][1]*scale)
        
        ctxArr[canvasId].stroke()
        ctxArr[canvasId].fill()
        // if(SLEEP_T) await new Promise(r => setTimeout(r, SLEEP_T));

    }
// [ 5561, 66437 ][ 94737, 50322 ]
// ((4615,66437),(94737,50322) <- g
}

function calcArea([x1,y1],[x2,y2]){
    return (Math.abs(x1-x2)+1)*(Math.abs(y1-y2)+1)
}

function inArea(P,points) {


    const x = P[0], y = P[1];
    let inside = false;

    const n = points.length;
    let j = n - 1;

    for (let i = 0; i < n; j = i++) {

        const xi = points[i][0], yi = points[i][1];
        const xj = points[j][0], yj = points[j][1];

        if ((yi > y) !== (yj > y)) {
            const xInt = (xj - xi) * (y - yi) / (yj - yi) + xi;
            if (x < xInt) inside = !inside;
        }
    }

    return inside;
}

function segmentsIntersect(A, B, C, D) {
    function orient(P, Q, R) {
        return (Q[0] - P[0]) * (R[1] - P[1]) - (Q[1] - P[1]) * (R[0] - P[0]);
    }

    const o1 = orient(A, B, C);
    const o2 = orient(A, B, D);
    const o3 = orient(C, D, A);
    const o4 = orient(C, D, B);

    // Proper intersection (strict)
    return (o1 * o2 < 0 && o3 * o4 < 0);
}

function segmentInsidePolygon(A, B, points) {

    // --- 1) Oba końce muszą być w środku ---
    if (!inArea(A,points) || !inArea(B,points)) return false;

    // --- 2) Odcinek AB nie może przecinać żadnej krawędzi polygonu ---
    const n = points.length;

    for (let i = 0; i < n; i++) {
        const C = points[i];
        const D = points[(i + 1) % n];

        // Pomijamy przypadek gdy krawędź zaczyna/kończy się w A lub B
        // (bo to nadal jest "wewnątrz")
        if (
            (C[0] === A[0] && C[1] === A[1]) ||
            (C[0] === B[0] && C[1] === B[1]) ||
            (D[0] === A[0] && D[1] === A[1]) ||
            (D[0] === B[0] && D[1] === B[1])
        ) continue;

        if (segmentsIntersect(A, B, C, D)) {
            return false;
        }
    }

    // --- 3) Dodatkowe bezpieczeństwo: środek odcinka też musi być w środku ---
    const mid = [(A[0] + B[0]) / 2, (A[1] + B[1]) / 2];
    if (!inArea(mid,points)) return false;

    return true;
}


function isValidRect([xA,yA],[xC,yC],points){
    const A = [xA,yA]
    const B = [xC,yA]
    const C = [xC,yC]
    const D = [xA,yC]

    for(let [P,Q] of [[A,B],[B,C],[C,D],[D,A]]){
        if(!segmentInsidePolygon(P,Q,points)) 
            {
                // console.log(A,B,C,D)
                // cleanCanvas(1)
                // drawArea(P,Q,"purple","purple",1)
                return false
            }
    }

    return true

}

async function part2(points){

    // await drawPoints(points)
    await connectPoints(points)

    let maxArea = 0
    let maxA,maxB

    for(let idxA=0; idxA<points.length; idxA++){
        break
        for(let idxB=idxA+1; idxB<points.length; idxB++){
            
        // idxA = 1
        // idxB = 216

        let A = points[idxA]
        let B = points[idxB]

        // console.log("VALID?",isValidRect(A,B,points))
        // cleanCanvas(1)
        // drawArea(A,B,"#f00","#ff000010",1)
        // return

        if(!isValidRect(A,B,points)) continue
        if(SLEEP_T) await new Promise(r => setTimeout(r, SLEEP_T));
        cleanCanvas(1)
        drawArea(A,B,"#f00","#ff000010",1)
        
        area = calcArea(A,B)
        if(area>maxArea){
            maxArea = area
            maxA = A
            maxB = B
        }
        displayPart2.innerText = maxArea

        }
    }

    // cleanCanvas(1)
    // drawArea(maxA,maxB,"#ffff00","ffff0010",1)
    
// ((4615,66437),(94737,50322) <- g
    correctA = [4615,66437]
    correctB = [94737,50322]
    drawArea(correctA,correctB,"#ff00ff","#ff00ff10",0)
    console.log(calcArea(correctA,correctB))
    console.log(isValidRect(correctA,correctB,points))

    drawArea
    displayPart2.innerText = `-> ${displayPart2.innerText}`
    // console.log(maxA,maxB)
    console.error("FIN")

}