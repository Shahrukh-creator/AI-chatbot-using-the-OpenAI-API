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

  messages: ChatMessage[] = [];
  draft = '';
  loading = false;
  error = '';

  send(): void {
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
          { role: 'assistant', content: response.reply },
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
}
