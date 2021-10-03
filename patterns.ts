function pattern1(rows:number) {
    [...Array(rows).keys()].forEach(() => {
        console.log("*")
    });
}