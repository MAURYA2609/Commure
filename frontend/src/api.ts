// Every backend call goes through here. Relative paths like /api/... hit the
// Vite proxy, so the browser sees one origin and CORS never comes up in dev.
export class ApiError extends Error {
  readonly status: number;

  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

export async function api<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers = new Headers(options.headers);
  if (options.body !== undefined) headers.set("Content-Type", "application/json");

  let response: Response;
  try {
    response = await fetch(path, { ...options, headers });
  } catch (err) {
    if (err instanceof DOMException && err.name === "AbortError") throw err;
    throw new ApiError(0, "Network error: is the backend running on port 8000?");
  }

  if (!response.ok) {
    const body = await response.json().catch(() => null);
    const detail = body?.detail;
    throw new ApiError(response.status, typeof detail === "string" ? detail : response.statusText);
  }
  return (response.status === 204 ? undefined : await response.json()) as T;
}

export function errorMessage(err: unknown): string {
  if (err instanceof ApiError) return err.status ? `${err.status}: ${err.message}` : err.message;
  return err instanceof Error ? err.message : String(err);
}