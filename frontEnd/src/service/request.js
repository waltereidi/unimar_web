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
            "Content-Type": "application/json",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "no-referrer-when-downgrade",
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
            "Access-Control-Allow-Origin": "*", 
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization"
        }

    }
    addHeaders(headers = {}, key, value) {
    return { ...headers, [key]: value };
    }

    withAuth(headers = {}) {
    headers['Authorization'] = `Bearer ${this.authStore.token ?? ""}`;
    return headers;
    }

    async get(endpoint = '', headers = {}) {
    headers = this.withAuth({ ...this.getDefaultHeaders(), ...headers });
    const response = await fetch(`${this.API_URL}${endpoint}`, {
        method: 'GET',
        headers:headers,
        
    });

    if(response.status == 401)
            this.clearToken()
        
    return response.json();
    }

    async post(endpoint = '', body = {}, headers = {}) {
        headers = this.withAuth(headers);
            const response = await fetch(`${this.API_URL}${endpoint}`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(body),
        });
        if(response.status == 401)
            this.clearToken()
        return response;
    }
}
