const { ipcMain } = require('electron');
const electron = require('electron');
const fs = require('fs');
const { exit } = require('process');
const {dialog} = electron;
const app = electron.app;
const Window = electron.BrowserWindow;
const {ipc} = electron;
const ts = require("typescript")

let win;
let win2;

app.on("ready",() => {
    win = new Window({
        width:800,
        height:800,
        minHeight:800,
        minWidth:800,
        maxHeight:800,
        maxWidth:800,
        webPreferences: {
            nodeIntegration: true
        }
    });
    win.loadFile('login.html')
})


//communication with renderer

ipcMain.on('execute',(event,text) => {

    // let sourceCode = text;
    // let tsSourceFile = ts.createSourceFile(
    //     __filename,
    //     sourceCode,
    //     ts.ScriptTarget.Latest
    //   );
    // console.log(tsSourceFile);
    let x = text.indexOf("createCanvas");
    console.log(x);

    fs.writeFileSync('template/sketch.js',text,(err) => {
        if(err){
            console.log('BUFFER FILE ERROR');
        };
    })

    win2 = new Window({
        width: 600,
        height:600
    });
    win2.loadFile('template/test.html');
})

ipcMain.on('save', (event,text)=> {
    let path = dialog.showSaveDialogSync(win,{defaultPath: "save.txt"});
    if(path)
    {
        fs.writeFile(path,text,(err)=>{
            if(err){
                console.log("ERROR");
            }
        console.log("File saved.")
    })
    }
});
