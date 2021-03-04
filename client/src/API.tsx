import React from "react";

export const fetchCloudProviders = async (provider: string, nearest: number, latitude: string, longitude: string) => {
    const endpoint = `http://127.0.0.1:8000/provider/clouds?provider=${provider}&nearest=${nearest}&latitude=${latitude}&longitude=${longitude}`
    const data = await (await fetch(endpoint)).json();
    return data;
};