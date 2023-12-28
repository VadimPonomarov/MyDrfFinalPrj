import React from 'react';

import './App.scss';
import {Stack, Typography} from "@mui/material";

import MyTopography from "./components/MyTopography";

function App() {
    return (
        <Stack className="App">
            <header className="App-header">
                App header
            </header>
            <Typography variant={"h2"} component={"address"} color={"burlywood"}>
                <MyTopography/>
            </Typography>
            <Typography variant={"h1"}>
                hgkhgkhk
            </Typography>

        </Stack>
    );
}

export default App;
