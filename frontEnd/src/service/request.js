import { useAuthStore } from '@/stores/auth'
// Classe filha que herda de BaseRequest
export class Request  {
    constructor() {
        this.authStore = useAuthStore();
        this.API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
    }
    setToken(token ){
        this.authStore.setToken(token );
    }
    clearToken(){
        this.authStore.clearToken();
    }
    getDefaultHeaders() {
        return {
        'Content-Type': 'application/json',
        };
    }
    addHeaders(headers = {}, key, value) {
    return { ...headers, [key]: value };
    }

    withAuth(headers = {}) {
    console.log(headers)
    headers['Authorization'] = `Bearer ${this.authStore.token ?? ""}`;
    console.log(headers)
    return headers;
    }

    async get(endpoint = '', headers = {}) {
    headers = this.withAuth({ ...this.getDefaultHeaders(), ...headers });
    const response = await fetch(`${this.API_URL}${endpoint}`, {
        method: 'GET',
        headers:headers,
        
    });
    return response.json();
    }

    async post(endpoint = '', body = {}, headers = {}) {
        headers = this.withAuth(headers);

        const response = fetch(`${this.API_URL}${endpoint}`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(body),
        });
    
        return response;
    }
}
