import React from "react";

export const fetchCloudProviders = async (provider: string, nearest: string, latitude: string, longitude: string) => {
    const endpoint = `http://localhost:8000/provider/clouds?provider=${provider}&nearest=${nearest}&latitude=${latitude}&longitude=${longitude}`
    const data = await (await fetch(endpoint)).json();
    return data;
};