import { useState } from 'react';
import axios from 'axios';
import SAPSampleData from '../../sap-sample-data.ts';

function AiForecastNaive() {
    const [response, setResponse] = useState<any>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleForecast = async () => {
        setLoading(true);
        try {
            const payload = {
                SE16N_MARA: SAPSampleData.SE16N_MARA,
                SalesOrderReport: SAPSampleData.SalesOrderReport
            };

            const res = await axios.post(
                `${import.meta.env.VITE_API_URL}/sales-prediction-naive`,
                payload,
                {
                    headers: {
                        Accept: 'application/json',
                        'Content-Type': 'application/json',
                    }
                }
            );

            setResponse(res.data);
            setError(null);
        } catch (err: any) {
            setError(err.message || 'An error occurred');
            setResponse(null);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container mt-4">
            <h1 className="mb-4">📊 AI Forecast (Naive)</h1>

            <button className="btn btn-primary mb-3" onClick={handleForecast} disabled={loading}>
                {loading ? 'Loading...' : 'Run Forecast'}
            </button>

            {error && <div className="alert alert-danger">{error}</div>}

            {response?.summary && (
                <div className="alert alert-info">
                    <strong>Total Products:</strong> {response.summary.totalProducts} <br />
                    <strong>Average Forecasted Sales (Next Quarter):</strong> {response.summary.averageForecastedSalesNextQuarter}
                </div>
            )}

            {response?.products?.length > 0 && (
                <div className="table-responsive">
                    <table className="table table-bordered table-striped">
                        <thead className="table-dark">
                            <tr>
                                <th>Material</th>
                                <th>Type</th>
                                <th>Unit</th>
                                <th>Total Quantity</th>
                                <th>Total Net Value</th>
                                <th>Avg Monthly Sales</th>
                                <th>Forecast Q3</th>
                                <th>Plant</th>
                                <th>Company Code</th>
                                <th>Product Group</th>
                                <th>Division</th>
                            </tr>
                        </thead>
                        <tbody>
                            {response.products.map((item: any, idx: number) => (
                                <tr key={idx}>
                                    <td>{item.MaterialNumber}</td>
                                    <td>{item.MaterialType}</td>
                                    <td>{item.Unit}</td>
                                    <td>{item.TotalSalesQuantity}</td>
                                    <td>{item.TotalNetValue}</td>
                                    <td>{item.AvgMonthlySales}</td>
                                    <td>{item.ForecastNextQuarter}</td>
                                    <td>{item.KeyConstraints.Plant}</td>
                                    <td>{item.KeyConstraints.CompanyCode}</td>
                                    <td>{item.KeyConstraints.ProductGroup}</td>
                                    <td>{item.KeyConstraints.Division}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}

export default AiForecastNaive;