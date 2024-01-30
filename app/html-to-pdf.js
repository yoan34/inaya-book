const puppeteer = require('puppeteer');
const path = require('path');
const fs = require("fs").promises;


async function createPdfWithHTMLFiles(bookName) {

    console.log(path.dirname(__dirname))
    const bookPath = `${path.dirname(__dirname)}/book/${bookName}`
    const resultPath = `${path.dirname(__dirname)}/book/result_${bookName}`

    try {
        let htmlFiles = await fs.readdir(bookPath);
        console.log(htmlFiles);
        const browser = await puppeteer.launch();

        for (const file of htmlFiles) {
            const page = await browser.newPage();
            await page.goto(`file://${bookPath}/${file}`, { waitUntil: 'networkidle0' });

            console.log(`${resultPath}/${path.parse(file).name}.pdf`)
            await page.pdf({
                path: `${resultPath}/${path.parse(file).name}.pdf`,
                format: 'A4',
                printBackground: true,
                landscape: true,
                margin: { top: 0, right: 0, bottom: 0, left: 0 }
            });

            await page.close();
        }

        await browser.close();

    } catch (err) {
        console.log("Erreur:", err);
    }
}

// const categories = [
//   "adjectifs demonstratifs",
//   "adjectifs possessifs deuxieme personne",
//   "adjectifs possessifs pluriel",
//   "adjectifs possessifs premiere personne",
//   "adjectifs possessifs troisieme personne",
//   "articles definis",
//   "articles indefinis",
//   "articles partitifs"
// ]
const categories = [
  "img",
]
createPdfWithHTMLFiles("book1")