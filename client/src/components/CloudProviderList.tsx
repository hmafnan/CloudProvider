import React from "react";
import {fetchCloudProviders} from "../API";


const CloudProviderList: React.FC = () => {
    const [provider, setProvider] = React.useState('all')
    const [latitude, setLatitude] = React.useState('0');
    const [longitude, setLongitude] = React.useState('0');
    const [clouds, setClouds] = React.useState([{
        cloud_description: '',
        cloud_name: '',
        geo_region: ''
    }])

    const setCoords = () => {
        // Logic to set current coordinates
        // Copied from the following url
        // https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates/longitude

        navigator.geolocation.getCurrentPosition(function(position) {
            let lat = position.coords.latitude;
            let long = position.coords.longitude;

            setLatitude(lat.toFixed(2));
            setLongitude(long.toFixed(2));
        });
    }

    const getData = async () => {
        setCoords();
        setClouds(await fetchCloudProviders(provider, 1, latitude, longitude));
    }

    const providerChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setProvider(event.target.value);
        getData();
    }

    const renderTableData = () => {
      return clouds.map((cloud, index) => {
         const { cloud_description, cloud_name, geo_region } = cloud //destructuring
         return (
            <tr key={index}>
               <td>{cloud_name}</td>
               <td>{geo_region}</td>
               <td>{cloud_description}</td>
            </tr>
         )
      })
   }

    return (
        <div className="providers_list">
            <h2 className="display-6" style={{color:"#FF524D"}}>Available Cloud Providers</h2>
            <div className="row">
                <div className="col-4">
                    <select className="form-select form-select-sm"
                            aria-label=".form-select-sm example" value={provider}
                            onChange={providerChange}>
                        <option value="all">All Providers</option>
                        <option value="aws">Amazon Web Services</option>
                        <option value="google">Google Cloud Platform</option>
                    </select>
                </div>
                <div className="col-4">
                    <div className="form-check">
                        <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" />
                            <label className="form-check-label" htmlFor="flexCheckDefault">
                                Nearest Region
                            </label>
                    </div>
                </div>
                <div className="col-4">
                    <button onClick={getData} className="btn btn-primary pull-right">Get Data</button>
                </div>
            </div>

            <table className="table table-striped table-bordered mt-3">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Region</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    {renderTableData()}
                </tbody>
            </table>
        </div>
    )
}

export default CloudProviderList;