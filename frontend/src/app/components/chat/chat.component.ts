import { CommonModule } from '@angular/common';
import { Component, ElementRef, ViewChild, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChatMessage } from '../../models/chat.models';
import { ChatService } from '../../services/chat.service';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css',
})
export class ChatComponent {
  private readonly chatService = inject(ChatService);

  @ViewChild('messageList') messageList?: ElementRef<HTMLDivElement>;
  selectedFile?: File;

  uploading = false;

  pdfUploaded = false;

  messages: ChatMessage[] = [];
  draft = '';
  loading = false;
  error = '';

  send(): void {
    this.error = '';   // clear any old errors

    if (!this.pdfUploaded) {

      this.error = "Please upload a PDF first.";
    
      return;
    }
    
    const text = this.draft.trim();
    if (!text || this.loading) {
      return;
    }

    const history = [...this.messages];
    this.messages = [...this.messages, { role: 'user', content: text }];
    this.draft = '';
    this.error = '';
    this.loading = true;
    this.scrollToBottom();

    this.chatService.sendMessage(text, history).subscribe({
      next: (response) => {
        this.messages = [
          ...this.messages,
          { role: 'assistant', content: response.answer },
        ];
        this.loading = false;
        this.scrollToBottom();
      },
      error: (err) => {
        this.error =
          err?.error?.detail ||
          'Could not reach the chatbot API. Is the Python backend running?';
        this.loading = false;
      },
    });
  }

  onKeydown(event: KeyboardEvent): void {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.send();
    }
  }

  private scrollToBottom(): void {
    queueMicrotask(() => {
      const el = this.messageList?.nativeElement;
      if (el) {
        el.scrollTop = el.scrollHeight;
      }
    });
  }

  onFileSelected(event: Event): void {

    const input = event.target as HTMLInputElement;
  
    if (!input.files?.length) {
      return;
    }
  
    const file = input.files[0];
  
    this.uploading = true;
  
    this.chatService.uploadPdf(file).subscribe({
  
      next: () => {
        this.error = '';           // <-- clear previous errors

        this.selectedFile = file;  // <-- you forgot this

        this.uploading = false;

        this.pdfUploaded = true;
  
        this.messages.push({
  
          role: 'assistant',
  
          content: `📄 "${file.name}" uploaded successfully. Ask me anything about it.`
  
        });
  
      },
  
      error: () => {
  
        this.uploading = false;
  
        this.error = "PDF upload failed.";
  
      }
  
    });
  
  }

  uploadPdf(): void {

    if (!this.selectedFile) {
      return;
    }
  
    this.uploading = true;
    this.error = '';
  
    this.chatService.uploadPdf(this.selectedFile).subscribe({
  
      next: () => {
  
        this.uploading = false;
        this.pdfUploaded = true;
  
        this.messages = [
          {
            role: 'assistant',
            content: '✅ PDF uploaded successfully. You can now ask questions.'
          }
        ];
      },
  
      error: () => {
  
        this.uploading = false;
  
        this.error = 'PDF upload failed.';
      }
  
    });
  
  }

  
}
