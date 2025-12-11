const FILE = "input"
const SLEEP_T = 1

async function main(){

    let points = await loadPoints(FILE)
    setUpCanvases(points)

    // PART 1
    // await part1(points)
    displayPart1.innerText = `-> ${displayPart1.innerText}`

    //PART 2
    await part2(points)
}
main()


    // PART 2: 1452422268  /  (4615,66437),(94737,50322)