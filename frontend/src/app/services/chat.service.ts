import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { environment } from '../../environments/environment';
import { ChatMessage, ChatResponse } from '../models/chat.models';

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  private readonly http = inject(HttpClient);

  uploadPdf(file: File): Observable<any> {

    const formData = new FormData();

    formData.append("file", file);

    return this.http.post(
      `${environment.apiUrl}/upload`,
      formData
    );
  }

  sendMessage(
    message: string,
    history: ChatMessage[]
  ): Observable<ChatResponse> {

    return this.http.post<ChatResponse>(
      `${environment.apiUrl}/chat`,
      {
        question: message
      }
    );
  }
}