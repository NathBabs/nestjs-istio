import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return `Good afternoon ${new Date().toISOString()} 👮🏽`;
  }
}
